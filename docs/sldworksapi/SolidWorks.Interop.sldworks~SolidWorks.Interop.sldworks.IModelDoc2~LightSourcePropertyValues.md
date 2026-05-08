# LightSourcePropertyValues Property (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues`

Gets and sets the light source property values.
Gets and sets the light source property values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LightSourcePropertyValues( _
   ByVal ID As System.Integer _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim ID As System.Integer
Dim value As System.Object
 
instance.LightSourcePropertyValues(ID) = value
 
value = instance.LightSourcePropertyValues(ID)
```

```

System.object LightSourcePropertyValues( 
   System.int ID
) {get; set;}
```

```

property System.Object^ LightSourcePropertyValues {
   System.Object^ get(System.int ID);
   void set (System.int ID, System.Object^ value);
}
```

#### Parameters

*ID*
:   Light source ID

#### Property Value

Array of 19 doubles containing the light source properties (see **Remarks**)

Remarks

The light source ID ranges from 0 to n, where n = (the total number of light sources - 1). To get the total number of light sources, use [IModelDoc2::GetLightSourceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceCount.md).

The return values for this property is the following array of 19 doubles:

[ type, Intensity, Color[3], Position[3], Direction[3], coneAngle, falloff[3], Ambient, Specular, isDisabled, SpotExponent ]

where:

- type =  an integer packed into a double that represents the light source type where valid types are taken from openGL definitions (LIGHT\_EYE, LIGHT\_AMBIENT, LIGHT\_SPOT, LIGHT\_POINT, LIGHT\_DISTANT)
- Intensity = Light-source intensity (diffuseness) where values range from 0 to 1.
- Color[3] =  Light-source color in the form of an array of 3 doubles (R, G, B) where values range from 0 to 1.
- Position[3] =  Light-source position for spot lights in the form of an array of 3 doubles (X, Y, Z) in model space.
- Direction[3] = Light-source direction in the form of an array of 3 doubles (i, j, k)
- coneAngle = Light-source cone half angle in degrees where valid values are from 0 to 90 and 180.
- falloff[3] =  Light-source falloff in the form of an array of 3 doubles (Kc, Kl, Kq). These values result in changes in light intensity as the distance between the light position and the vertex change.  
    
  **NOTE:**The falloff[3] values are not supported in SOLIDWORKS 2011 and later.  
    
  The result is driven by the following equation:

 [ 1 / (Kc + D\*Kl + D\*D\*Kq ) ]

  where:

D =  the distance.between the light's position and the vertex

Kc = constant attenuation

Kl = linear attenuation

Kq = quadratic attenuation

- Ambient = light-source ambient Intensity
- Specular = light-source specular Intensity
- isDisabled = an integer packed into a double. True means that the light is disabled and false means the light is not disabled.
- SpotExponent = spot exponent  
    
  **NOTE:** The SpotExponent value is not supported in SOLIDWORKS 2011 and later.

Example

[Redirect Spotlight (VBA)](Redirect_Spotlight_Example_VB.htm)  
[Turn Lights On (VBA)](Turn_Lights_On_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ILightSourcePropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ILightSourcePropertyValues.md)  
[IModelDoc2::LightSourceUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourceUserName.md)  
[IModelDoc2::AddLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSource.md)  
[IModelDoc2::AddLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSourceExtProperty.md)  
[IModelDoc2::DeleteLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteLightSource.md)  
[IModelDoc2::GetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceExtProperty.md)  
[IModelDoc2::GetLightSourceIdFromName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.md)  
[IModelDoc2::GetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceName.md)  
[IModelDoc2::ResetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetLightSourceExtProperty.md)  
[IModelDoc2::SetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourceName.md)  
[IModelDoc2::SetLightSourcePropertyValuesVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourcePropertyValuesVB.md)  
[IModelDocExtension::GetSunLightSourcePropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightSourcePropertyValues.md)  
[IModelDocExtension::SetSunLightSourcePropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightSourcePropertyValues.md)
