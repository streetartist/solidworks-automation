# GetCoordinateSystemTransformByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCoordinateSystemTransformByName`

Gets the transform of the specified coordinate system.
Gets the transform of the specified coordinate system.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCoordinateSystemTransformByName( _
   ByVal NameIn As System.String _
) As MathTransform
```

```

Dim instance As IModelDocExtension
Dim NameIn As System.String
Dim value As MathTransform
 
value = instance.GetCoordinateSystemTransformByName(NameIn)
```

```

MathTransform GetCoordinateSystemTransformByName( 
   System.string NameIn
)
```

```

MathTransform^ GetCoordinateSystemTransformByName( 
   System.String^ NameIn
) 
```

#### Parameters

*NameIn*
:   Name of the coordinate system

#### Return Value

[Math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Example

[Get Coordinate System Transform (VBA)](Get_Coordinate_System_Transform_Example_VB.htm)  
[Get Table-driven Pattern Properties (VBA)](Get_Table-driven_Pattern_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::GetCurrentCoordinateSystemName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetCurrentCoordinateSystemName.md)  
[IModelDoc2::InsertCoordinateSystem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCoordinateSystem.md)
