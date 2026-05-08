# GetCorresponding2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding2`

Gets the object in the underlying part or subassembly document that corresponds to the specified input object in this drawing view or assembly.
Gets the object in the underlying part or subassembly document that corresponds to the specified input object in this drawing view or assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCorresponding2( _
   ByVal InputObject As System.Object _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim InputObject As System.Object
Dim value As System.Object
 
value = instance.GetCorresponding2(InputObject)
```

```

System.object GetCorresponding2( 
   System.object InputObject
)
```

```

System.Object^ GetCorresponding2( 
   System.Object^ InputObject
) 
```

#### Parameters

*InputObject*
:   Object in this drawing view or assembly (see **Remarks**)

#### Return Value

Corresponding object in the underlying part or subassembly; null or Nothing if none found (see **Remarks**)

Remarks

InputObject can be any object assigned a persistent reference ID; for example, a [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md), [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) or [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) object.

To get the assembly object corresponding to a given component object, use [IComponent2::GetCorresponding](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorresponding.md).

To get the drawing view object corresponding to a given part or assembly object, use [IView::GetCorresponding](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCorresponding.md).

Example

[Get Corresponding Entities Between Parts and Drawing Views (VBA)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VB.htm)  
[Get Corresponding Entities Between Parts and Drawing Views (VB.NET)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VBNET.htm)  
[Get Corresponding Entities Between Parts and Drawing Views (C#)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetCorrespondingEntity2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity2.md)
