# GetModelDoc2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelDoc2`

Gets the model document for this component.
Gets the model document for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetModelDoc2() As System.Object
```

```

Dim instance As IComponent2
Dim value As System.Object
 
value = instance.GetModelDoc2()
```

```

System.object GetModelDoc2()
```

```

System.Object^ GetModelDoc2(); 
```

#### Return Value

[Model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)

Remarks

This method might return Nothing or null if:

- a component is suppressed or lightweight.
- the component ID is not loaded into memory by SOLIDWORKS.

For more information on lightweight components, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

When you use the IModelDoc2 object of a component, you do not have access to whatever uniqueness might exist for this instance of the assembly IComponent2. This occurs because the IModelDoc2 object goes back to the saved part file. By comparison, the IComponent2 object gathers information at the assembly level. This allows IComponent2 objects to recognize assembly-level changes made to a component instance (for example, assembly-level features and material changes).

In addition, the IModelDoc2 object returned from this method represents the last-saved state. If the component part is currently open, then the IModelDoc2 object represents the state of the opened document. For example, if the component part is not open and it was last saved in the default configuration, then IComponent2::GetModelDoc2  
returns a IModelDoc2 pointer representing that state. To get access to other configuration information (such as features and configuration properties), you must activate the part and show the desired configuration using [IModelDoc2::ShowConfiguration2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.md).

Unlike the previous version of this method ([IConfiguration::GetRootComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)), this version of this method can handle the root component of an assembly.

Example

[Get Selected Objects and types in Assembly (VBA)](Get_Selected_Objects_and_Types_in_Assembly_Example_VB.htm)  
[Insert MidSurface in Component (C#)](Insert_MidSurface_in_Component_Example_CSharp.htm)  
[Insert MidSurface in Component (VB.NET)](Insert_MidSurface_in_Component_Example_VBNET.htm)  
[Insert MidSurface in Component (VBA)](Insert_MidSurface_in_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::IsRoot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsRoot.md)
