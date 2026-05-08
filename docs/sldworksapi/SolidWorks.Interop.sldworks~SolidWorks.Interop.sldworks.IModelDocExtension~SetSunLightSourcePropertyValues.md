# SetSunLightSourcePropertyValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightSourcePropertyValues`

Sets the property values for a sunlight source.
Sets the property values for a sunlight source.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSunLightSourcePropertyValues( _
   ByVal NorthDirection As MathVector, _
   ByVal NorthLatitude As System.Double, _
   ByVal EastLongitude As System.Double, _
   ByVal TimeZone As System.Double, _
   ByVal DateTime As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim NorthDirection As MathVector
Dim NorthLatitude As System.Double
Dim EastLongitude As System.Double
Dim TimeZone As System.Double
Dim DateTime As System.String
Dim value As System.Boolean
 
value = instance.SetSunLightSourcePropertyValues(NorthDirection, NorthLatitude, EastLongitude, TimeZone, DateTime)
```

```

System.bool SetSunLightSourcePropertyValues( 
   MathVector NorthDirection,
   System.double NorthLatitude,
   System.double EastLongitude,
   System.double TimeZone,
   System.string DateTime
)
```

```

System.bool SetSunLightSourcePropertyValues( 
   MathVector^ NorthDirection,
   System.double NorthLatitude,
   System.double EastLongitude,
   System.double TimeZone,
   System.String^ DateTime
) 
```

#### Parameters

*NorthDirection*
:   [IMathVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md); north direction of the sunlight source

*NorthLatitude*
:   North latitude of the sunlight source

*EastLongitude*
:   East longitude of the sunlight source

*TimeZone*
:   Standard time zone of the sunlight source

*DateTime*
:   Date and time stamp in the specified TimeZone

#### Return Value

True if sunlight source property values are successfully set, false if not

Example

[Get and Set Sunlight Source Property Values (VBA)](Get_and_Set_Sunlight_Source_Property_Values_Example_VB.htm)  
[Get and Set Sunlight Source Property Values (VB.NET)](Get_and_Set_Sunlight_Source_Property_Values_Example_VBNET.htm)  
[Get and Set Sunlight Source Property Values (C#)](Get_and_Set_Sunlight_Source_Property_Values_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::SetLightSourcePropertyValuesVB Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourcePropertyValuesVB.md)  
[IModelDocExtension::GetSunLightSourcePropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightSourcePropertyValues.md)  
[IModelDoc2::LightSourcePropertyValues Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.md)  
[IModelDocExtension::SetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightAdvancedPropertyValues.md)
