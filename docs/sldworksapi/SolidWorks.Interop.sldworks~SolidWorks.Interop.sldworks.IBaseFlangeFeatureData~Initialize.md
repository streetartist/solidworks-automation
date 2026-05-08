# Initialize Method (IBaseFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize`

Initializes a newly created sheet metal base flange feature with the specified data.
Initializes a newly created sheet metal base flange feature with the specified data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Initialize( _
   ByVal UseMaterialSheetMetalParameters As System.Boolean, _
   ByVal OverrideDefaultBendAllowance As System.Boolean, _
   ByVal CustomBendAllowance As System.Object, _
   ByVal OverrideDefaultBendRelief As System.Boolean, _
   ByVal ReliefType As System.Integer, _
   ByVal UseReliefRatio As System.Boolean, _
   ByVal ReliefRatio As System.Double, _
   ByVal ReliefWidth As System.Double, _
   ByVal ReliefDepth As System.Double _
) 
```

```

Dim instance As IBaseFlangeFeatureData
Dim UseMaterialSheetMetalParameters As System.Boolean
Dim OverrideDefaultBendAllowance As System.Boolean
Dim CustomBendAllowance As System.Object
Dim OverrideDefaultBendRelief As System.Boolean
Dim ReliefType As System.Integer
Dim UseReliefRatio As System.Boolean
Dim ReliefRatio As System.Double
Dim ReliefWidth As System.Double
Dim ReliefDepth As System.Double
 
instance.Initialize(UseMaterialSheetMetalParameters, OverrideDefaultBendAllowance, CustomBendAllowance, OverrideDefaultBendRelief, ReliefType, UseReliefRatio, ReliefRatio, ReliefWidth, ReliefDepth)
```

```

void Initialize( 
   System.bool UseMaterialSheetMetalParameters,
   System.bool OverrideDefaultBendAllowance,
   System.object CustomBendAllowance,
   System.bool OverrideDefaultBendRelief,
   System.int ReliefType,
   System.bool UseReliefRatio,
   System.double ReliefRatio,
   System.double ReliefWidth,
   System.double ReliefDepth
)
```

```

void Initialize( 
   System.bool UseMaterialSheetMetalParameters,
   System.bool OverrideDefaultBendAllowance,
   System.Object^ CustomBendAllowance,
   System.bool OverrideDefaultBendRelief,
   System.int ReliefType,
   System.bool UseReliefRatio,
   System.double ReliefRatio,
   System.double ReliefWidth,
   System.double ReliefDepth
) 
```

#### Parameters

*UseMaterialSheetMetalParameters*
:   True to use the sheet metal properties of the applied material, false to not

*OverrideDefaultBendAllowance*
:   True to override the default bend allowance, false to not

*CustomBendAllowance*
:   [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md); valid only if OverrideDefaultBendAllowance is true

*OverrideDefaultBendRelief*
:   True to override the default bend relief, false to not

*ReliefType*
:   Relief type as defined in [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html); valid only if OverrideDefaultBendRelief is true

*UseReliefRatio*
:   True to use ReliefRatio, false to use ReliefWidth and ReliefDepth; valid only if OverrideDefaultBendRelief is true

*ReliefRatio*
:   Relief ratio; valid only if UseReliefRatio is true

*ReliefWidth*
:   Relief width (numerator of relief ratio); valid only if UseReliefRatio is false

*ReliefDepth*
:   Relief depth (denominator of relief ratio); valid only if UseReliefRatio is false

Remarks

After you call this method to initialize the base flange feature, you cannot change any of the properties associated with this method's parameters. After initialization you can get, but not set, the following using this interface:

- Whether to use default bend allowance
- Whether to use default bend relief
- Whether to use material sheet metal parameters
- Whether to use relief ratio
- Custom bend allowance
- Relief depth
- Relief ratio
- Relief type
- Relief width

You can, however, change any properties associated with the parent sheet metal after calling this method. For example:

- [ISheetMetalFeatureData::SetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetCustomBendAllowance.md)
- [ISheetMetalFeatureData::SetOverrideDefaultParameter2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetOverrideDefaultParameter2.md)
- [ISheetMetalFeatureData::AutoReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~AutoReliefType.md)
- [ISheetMetalFeatureData::ReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~ReliefRatio.md)
- [ISheetMetalFeatureData::UseMaterialSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~UseMaterialSheetMetalParameters.md)

See the Examples.

Example

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)  
[IBaseFlangeFeatureData::GetCustomBendAllowance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetCustomBendAllowance.md)  
[IBaseFlangeFeatureData::ReliefDepth Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefDepth.md)  
[IBaseFlangeFeatureData::ReliefRatio Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefRatio.md)  
[IBaseFlangeFeatureData::ReliefType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefType.md)  
[IBaseFlangeFeatureData::ReliefWidth Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefWidth.md)  
[IBaseFlangeFeatureData::UseDefaultBendAllowance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseDefaultBendAllowance.md)  
[IBaseFlangeFeatureData::UseDefaultBendRelief Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseDefaultBendRelief.md)  
[IBaseFlangeFeatureData::UseMaterialSheetMetalParameters Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseMaterialSheetMetalParameters.md)  
[IBaseFlangeFeatureData::UseReliefRatio Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseReliefRatio.md)
