# GetCSYSXYZAngularRotation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSXYZAngularRotation`

Gets the specified Tait-Bryan angular rotation values that transform one selected coordinate system into another.
Gets the specified Tait-Bryan angular rotation values that transform one selected coordinate system into another.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCSYSXYZAngularRotation( _
   ByRef XAngle As System.Double, _
   ByRef YAngle As System.Double, _
   ByRef ZAngle As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim XAngle As System.Double
Dim YAngle As System.Double
Dim ZAngle As System.Double
Dim value As System.Boolean
 
value = instance.GetCSYSXYZAngularRotation(XAngle, YAngle, ZAngle)
```

```

System.bool GetCSYSXYZAngularRotation( 
   out System.double XAngle,
   out System.double YAngle,
   out System.double ZAngle
)
```

```

System.bool GetCSYSXYZAngularRotation( 
   [Out] System.double XAngle,
   [Out] System.double YAngle,
   [Out] System.double ZAngle
) 
```

#### Parameters

*XAngle*
:   Angle of rotation between x axes

*YAngle*
:   Angle of rotation between y axes

*ZAngle*
:   Angle of rotation between z axes

#### Return Value

True if rotation values successfully retrieved, false if not

Remarks

This method corresponds to the SOLIDWORKS measure tool's calculation of angular rotation between two coordinate systems. See **SOLIDWORKS online help > Fundamentals > Measure Tool** for more information.

Use Wikipedia to learn about Tait-Bryan or Cardan angles.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetCSYSDistances Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSDistances.md)  
[IModelDocExtension::GetCSYSEulersAngularRotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSEulersAngularRotation.md)
