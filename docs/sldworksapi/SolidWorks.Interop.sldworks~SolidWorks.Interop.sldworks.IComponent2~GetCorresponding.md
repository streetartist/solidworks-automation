# GetCorresponding Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorresponding`

Gets the corresponding object in the context of the assembly for a specific instance of the component.
Gets the corresponding object in the context of the assembly for a specific instance of the component.

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

Dim instance As IComponent2
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
:   Pointer to the Dispatch object

#### Return Value

Pointer to the corresponding object in the context of the assembly for an instance of the component

Remarks

Given an object in an underlying component document, this method gets the corresponding object in the context of the assembly for a specific instance of that component document (i.e., there can be more than one instance).

You can use this method with any object assigned a persistent reference or object ID; for example, [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md),  [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md), [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md), [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md), etc.

Example

[Get Corresponding Objects in Assembly Component (C#)](Get_Corresponding_Objects_in_Assembly_Component_Example_CSharp.htm)  
[Get Corresponding Objects in Assembly Component (VB.NET)](Get_Corresponding_Objects_in_Assembly_Component_Example_VBNET.htm)  
[Get Corresponding Objects in Assembly Component (VBA)](Get_Corresponding_Objects_in_Assembly_Component_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.md)  
[IComponent2::IGetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetCorrespondingEntity.md)  
[IModelDocExtension::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding.md)  
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.md)
