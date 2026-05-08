# GetCSYSEulersAngularRotation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSEulersAngularRotation`

Gets the specified Eulers angular rotation values that transform one selected coordinate system into another.
Gets the specified Eulers angular rotation values that transform one selected coordinate system into another.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCSYSEulersAngularRotation( _
   ByRef phiAngle As System.Double, _
   ByRef thetaAngle As System.Double, _
   ByRef psiAngle As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim phiAngle As System.Double
Dim thetaAngle As System.Double
Dim psiAngle As System.Double
Dim value As System.Boolean
 
value = instance.GetCSYSEulersAngularRotation(phiAngle, thetaAngle, psiAngle)
```

```

System.bool GetCSYSEulersAngularRotation( 
   out System.double phiAngle,
   out System.double thetaAngle,
   out System.double psiAngle
)
```

```

System.bool GetCSYSEulersAngularRotation( 
   [Out] System.double phiAngle,
   [Out] System.double thetaAngle,
   [Out] System.double psiAngle
) 
```

#### Parameters

*phiAngle*
:   Roll or rotation about the longitudinal axis (see **Remarks**)

*thetaAngle*
:   Pitch or rotation about the lateral axis (see **Remarks**)

*psiAngle*
:   Yaw or rotation about the vertical axis (see **Remarks**)

#### Return Value

True if rotation values successfully retrieved, false if not

Remarks

phiAngle is the roll or rotation about the longitudinal axis. Rolling corresponds to moving one side of an object upward while moving the other side downward (no pitch or yaw).

thetaAngle is the pitch or rotation around the lateral axis. Pitching corresponds to tilting the front of an object up or down (no yaw or roll).

psiAngle is the yaw or rotation about the vertical axis. Yawing corresponds to turning the front of an object left or right (no pitch or roll).

This method corresponds to the SOLIDWORKS measure tool's calculation of angular rotation between two coordinate systems. See **SOLIDWORKS online help > Fundamentals > Measure Tool** for more information.

Use Wikipedia to learn more about Euler's angles.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetCSYSDistances Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSDistances.md)  
[IModelDocExtension::GetCSYSXYZAngularRotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSXYZAngularRotation.md)
