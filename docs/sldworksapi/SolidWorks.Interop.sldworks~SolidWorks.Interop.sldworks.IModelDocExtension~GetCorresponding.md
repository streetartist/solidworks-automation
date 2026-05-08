# GetCorresponding Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding`

Obsolete. Superseded by IModelDocExtension::GetCorresponding2.
Obsolete. Superseded by [IModelDocExtension::GetCorresponding2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCorresponding( _
   ByVal InputObject As System.Object _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim InputObject As System.Object
Dim value As System.Object
 
value = instance.GetCorresponding(InputObject)
```

```

System.object GetCorresponding( 
   System.object InputObject
)
```

```

System.Object^ GetCorresponding( 
   System.Object^ InputObject
) 
```

#### Parameters

*InputObject*
:   Pointer to the Dispatch object in the assembly context

#### Return Value

Pointer to the corresponding object in the underlying part, assembly, or subassembly document

Remarks

Given an object in an assembly context, this method gets the corresponding object in the underlying component document regardless of whether the document is a part or an assembly.

You can use this method with any object assigned a persistent reference ID; for example, a [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md), [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) or [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) object.

Example

[Get Corresponding Note in Assembly (VBA)](Get_Corresponding_Note_in_Assembly_Example_VB.htm)  
[Get Corresponding Note in Part (VBA)](Get_Corresponding_Note_in_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.md)  
[IComponent2::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorresponding.md)  
[IComponent2::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.md)  
[IComponent2::IGetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetCorrespondingEntity.md)
