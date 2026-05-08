# Initialize Method (IConvertSolidFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~Initialize`

Initializes this convert solid feature to have the specified properties.
Initializes this convert solid feature to have the specified properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Initialize( _
   ByVal UseMaterialSheetMetalParameters As System.Boolean, _
   ByVal UseGaugeTableParameters As System.Boolean, _
   ByVal CustomBendAllowance As System.Object _
) 
```

```

Dim instance As IConvertSolidFeatureData
Dim UseMaterialSheetMetalParameters As System.Boolean
Dim UseGaugeTableParameters As System.Boolean
Dim CustomBendAllowance As System.Object
 
instance.Initialize(UseMaterialSheetMetalParameters, UseGaugeTableParameters, CustomBendAllowance)
```

```

void Initialize( 
   System.bool UseMaterialSheetMetalParameters,
   System.bool UseGaugeTableParameters,
   System.object CustomBendAllowance
)
```

```

void Initialize( 
   System.bool UseMaterialSheetMetalParameters,
   System.bool UseGaugeTableParameters,
   System.Object^ CustomBendAllowance
) 
```

#### Parameters

*UseMaterialSheetMetalParameters*
:   True to use sheet metal parameters attached to the selected material, false to not (see **Remarks**)

*UseGaugeTableParameters*
:   True to use a gauge table values (material thickness, bend radius, and bend calculation method) as the basis of this feature, false to not

*CustomBendAllowance*
:   [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md)

Remarks

UseMaterialSheetMetalParameters is valid only if a material is applied to the solid.

Example

See the [IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)
