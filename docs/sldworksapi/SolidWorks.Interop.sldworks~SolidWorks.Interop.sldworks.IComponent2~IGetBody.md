# IGetBody Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBody`

Gets the body that belongs to this instance of this component.
Gets the body that belongs to this instance of this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBody() As Body2
```

```

Dim instance As IComponent2
Dim value As Body2
 
value = instance.IGetBody()
```

```

Body2 IGetBody()
```

```

Body2^ IGetBody(); 
```

#### Return Value

Pointer to the [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) object

Remarks

This method returns a valid IBody2 object only for fully resolved components that reference an [IPartDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md). For the root component, lightweight components or components that reference an AssemblyDoc, this method returns a NULL body object. However, if a component is in a multibody part, then this method returns the first body.

For COM applications, this method returns the status code ITF\_E\_COMPONENTNOTRESOLVED.

This method is different from the IPartDoc::Body method in that it recognizes assembly-level features and returns that information based on the component instance. IPartDoc::Body never recognizes assembly-level features because the feature information is kept with the assembly, not propagated down to the part file.

For example, if PartABC is added to an assembly twice, then changes to that IPartDoc object would affect both instances of the assembly IComponent2. Likewise, querying information from that IPartDoc object will not recognize changes in the assembly that may have altered only one of the components (for example, an assembly-level feature was added to one of the components). However, the component object recognizes the two instances of PartABC as two distinct IComponent2 objects and returns its information from the assembly level.

For example, one assembly configuration might have an assembly-level feature that cuts a hole through each of the components in the assembly. Using this method on each of the assembly components returns the body of each component with the hole feature that was applied in this particular configuration. If you switch to the configuration  
without the assembly-level hole and re-traverse the IComponent2 objects, then calling this method for each component returns the IBody2 object without the hole feature because it was applied in the other configuration.

For more information on lightweight components, see [IComponent2::GetSuppression](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.md), [IComponent2::SetSuppression2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.md), and [IAssemblyDoc::ResolveAllLightWeightComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents.md).

Example

[Enumerate Bodies (C++)](Enumerate_Bodies_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBody.md)  
[IComponent2::GetBodies3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies3.md)  
[IComponent2::EnumBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies2.md)
