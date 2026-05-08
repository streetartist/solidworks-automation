# SetLightSourcePropertyValuesVB Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourcePropertyValuesVB`

Sets the light source property values.
Sets the light source property values.

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

Dim instance As IModelDoc2
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
:   Light source ID name

*LType*
:   Light source type; valid types are taken from openGL definitions (LIGHT\_EYE, LIGHT\_AMBIENT, LIGHT\_SPOT, LIGHT\_POINT, LIGHT\_DISTANT)

*Diff*
:   Light source diffuseness where values range from 0 to 1

*RgbColor*
:   Color value

*Dist*
:   Distance between the light source position and the vertex

*DirX*
:   X unit vector value describing the lights position

*DirY*
:   Y unit vector value describing the lights po

*DirZ*
:   Z unit vector value describing the lights position

*SpotDirX*
:   Spot X direction

*SpotDirY*
:   Spot Y direction

*SpotDirZ*
:   Spot Z direction

*SpotAngle*
:   Spot angle

*FallOff0*
:   Light source falloff - constant attenuation

    **NOTE:** This parameter is not supported in SOLIDWORKS 2011 and later.

*FallOff1*
:   Light source falloff - linear attenuation

    **NOTE:** This parameter is not supported in SOLIDWORKS 2011 and later.

*FallOff2*
:   Light source falloff - quadratic attenuation

    **NOTE:** This parameter is not supported in SOLIDWORKS 2011 and later.

*Ambient*
:   Light source ambient intensity

*Specular*
:   Light source specular intensity

*SpotExponent*
:   Spot exponent

    **NOTE:** This parameter is not supported in SOLIDWORKS 2011 and later.

*BDisable*
:   Light source disabled

#### Return Value

True if setting the light source properties is successful, false if not

Remarks

This method is similar to [IModelDoc2::LightSourcePropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.md) and [IModelDoc2::ILightSourcePropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ILightSourcePropertyValues.md), except using this method you can pass each argument individually.

Example

[Add Spotlight and Get Light Feature (C#)](Add_Spotlight_and_Get_Light_Feature_Example_CSharp.htm)  
[Add Spotlight and Get Light Feature (VB.NET)](Add_Spotlight_and_Get_Light_Feature_Example_VBNET.htm)  
[Add Spotlight and Get Light Feature (VBA)](Add_Spotlight_and_Get_Light_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::AddLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSource.md)  
[IModelDoc2::AddLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSourceExtProperty.md)  
[IModelDoc2::AddLightToScene Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightToScene.md)  
[IModelDoc2::AddSceneExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddSceneExtProperty.md)  
[IModelDoc2::DeleteLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteLightSource.md)  
[IModelDoc2::GetLightSourceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceCount.md)  
[IModelDoc2::GetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceExtProperty.md)  
[IModelDoc2::GetLightSourceIdFromName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.md)  
[IModelDoc2::GetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceName.md)  
[IModelDoc2::Lights Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Lights.md)  
[IModelDoc2::ResetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetLightSourceExtProperty.md)  
[IModelDoc2::ResetSceneExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetSceneExtProperty.md)  
[IModelDoc2::SetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourceName.md)
