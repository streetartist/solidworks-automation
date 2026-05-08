# SetLightSourcePropertyValuesVB Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetLightSourcePropertyValuesVB`

Obsolete. Superseded by IModelDoc2::SetLightSourcePropertyValuesVB.
Obsolete. Superseded by [IModelDoc2::SetLightSourcePropertyValuesVB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourcePropertyValuesVB.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLightSourcePropertyValuesVB( _
   ByVal IdName As System.String, _
   ByVal LType As System.Integer, _
   ByVal Diff As System.Double, _
   ByVal RgbColor As System.Integer, _
   ByVal Dist As System.Double, _
   ByVal DirX As System.Double, _
   ByVal DirY As System.Double, _
   ByVal DirZ As System.Double, _
   ByVal SpotDirX As System.Double, _
   ByVal SpotDirY As System.Double, _
   ByVal SpotDirZ As System.Double, _
   ByVal SpotAngle As System.Double, _
   ByVal FallOff0 As System.Double, _
   ByVal FallOff1 As System.Double, _
   ByVal FallOff2 As System.Double, _
   ByVal Ambient As System.Double, _
   ByVal Specular As System.Double, _
   ByVal SpotExponent As System.Double, _
   ByVal BDisable As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim IdName As System.String
Dim LType As System.Integer
Dim Diff As System.Double
Dim RgbColor As System.Integer
Dim Dist As System.Double
Dim DirX As System.Double
Dim DirY As System.Double
Dim DirZ As System.Double
Dim SpotDirX As System.Double
Dim SpotDirY As System.Double
Dim SpotDirZ As System.Double
Dim SpotAngle As System.Double
Dim FallOff0 As System.Double
Dim FallOff1 As System.Double
Dim FallOff2 As System.Double
Dim Ambient As System.Double
Dim Specular As System.Double
Dim SpotExponent As System.Double
Dim BDisable As System.Boolean
Dim value As System.Boolean
 
value = instance.SetLightSourcePropertyValuesVB(IdName, LType, Diff, RgbColor, Dist, DirX, DirY, DirZ, SpotDirX, SpotDirY, SpotDirZ, SpotAngle, FallOff0, FallOff1, FallOff2, Ambient, Specular, SpotExponent, BDisable)
```

```

System.bool SetLightSourcePropertyValuesVB( 
   System.string IdName,
   System.int LType,
   System.double Diff,
   System.int RgbColor,
   System.double Dist,
   System.double DirX,
   System.double DirY,
   System.double DirZ,
   System.double SpotDirX,
   System.double SpotDirY,
   System.double SpotDirZ,
   System.double SpotAngle,
   System.double FallOff0,
   System.double FallOff1,
   System.double FallOff2,
   System.double Ambient,
   System.double Specular,
   System.double SpotExponent,
   System.bool BDisable
)
```

```

System.bool SetLightSourcePropertyValuesVB( 
   System.String^ IdName,
   System.int LType,
   System.double Diff,
   System.int RgbColor,
   System.double Dist,
   System.double DirX,
   System.double DirY,
   System.double DirZ,
   System.double SpotDirX,
   System.double SpotDirY,
   System.double SpotDirZ,
   System.double SpotAngle,
   System.double FallOff0,
   System.double FallOff1,
   System.double FallOff2,
   System.double Ambient,
   System.double Specular,
   System.double SpotExponent,
   System.bool BDisable
) 
```

#### Parameters

*IdName*

*LType*

*Diff*

*RgbColor*

*Dist*

*DirX*

*DirY*

*DirZ*

*SpotDirX*

*SpotDirY*

*SpotDirZ*

*SpotAngle*

*FallOff0*

*FallOff1*

*FallOff2*

*Ambient*

*Specular*

*SpotExponent*

*BDisable*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
