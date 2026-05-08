# GetSunLightSourcePropertyValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightSourcePropertyValues`

Gets the property values for a sunlight source.
Gets the property values for a sunlight source.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSunLightSourcePropertyValues( _
   ByRef NorthDirection As MathVector, _
   ByRef NorthLatitude As System.Double, _
   ByRef EastLongitude As System.Double, _
   ByRef TimeZone As System.Double, _
   ByRef DateTime As System.String _
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
 
value = instance.GetSunLightSourcePropertyValues(NorthDirection, NorthLatitude, EastLongitude, TimeZone, DateTime)
```

```

System.bool GetSunLightSourcePropertyValues( 
   out MathVector NorthDirection,
   out System.double NorthLatitude,
   out System.double EastLongitude,
   out System.double TimeZone,
   out System.string DateTime
)
```

```

System.bool GetSunLightSourcePropertyValues( 
   [Out] MathVector^ NorthDirection,
   [Out] System.double NorthLatitude,
   [Out] System.double EastLongitude,
   [Out] System.double TimeZone,
   [Out] System.String^ DateTime
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
:   Date and time stamp in the specified TimeZone

#### Return Value

True if getting the value is successful, false if not

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
[IModelDocExtension::SetSunLightSourcePropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightSourcePropertyValues.md)  
[IModelDoc2::LightSourcePropertyValues Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.md)  
[IModelDocExtension::GetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightAdvancedPropertyValues.md)
