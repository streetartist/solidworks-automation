# EditDimensionProperties Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditDimensionProperties`

Edits the selected dimension.
Edits the selected dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditDimensionProperties( _
   ByVal TolType As System.Integer, _
   ByVal TolMax As System.Double, _
   ByVal TolMin As System.Double, _
   ByVal TolMaxFit As System.String, _
   ByVal TolMinFit As System.String, _
   ByVal UseDocPrec As System.Boolean, _
   ByVal Precision As System.Integer, _
   ByVal ArrowsIn As System.Integer, _
   ByVal UseDocArrows As System.Boolean, _
   ByVal Arrow1 As System.Integer, _
   ByVal Arrow2 As System.Integer, _
   ByVal PrefixText As System.String, _
   ByVal SuffixText As System.String, _
   ByVal ShowValue As System.Boolean, _
   ByVal CalloutText1 As System.String, _
   ByVal CalloutText2 As System.String, _
   ByVal DimensionLowerText As System.String, _
   ByVal CenterText As System.Boolean, _
   ByVal ConfigOption As System.Integer, _
   ByVal ConfigNames As System.Object _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim TolType As System.Integer
Dim TolMax As System.Double
Dim TolMin As System.Double
Dim TolMaxFit As System.String
Dim TolMinFit As System.String
Dim UseDocPrec As System.Boolean
Dim Precision As System.Integer
Dim ArrowsIn As System.Integer
Dim UseDocArrows As System.Boolean
Dim Arrow1 As System.Integer
Dim Arrow2 As System.Integer
Dim PrefixText As System.String
Dim SuffixText As System.String
Dim ShowValue As System.Boolean
Dim CalloutText1 As System.String
Dim CalloutText2 As System.String
Dim DimensionLowerText As System.String
Dim CenterText As System.Boolean
Dim ConfigOption As System.Integer
Dim ConfigNames As System.Object
Dim value As System.Boolean
 
value = instance.EditDimensionProperties(TolType, TolMax, TolMin, TolMaxFit, TolMinFit, UseDocPrec, Precision, ArrowsIn, UseDocArrows, Arrow1, Arrow2, PrefixText, SuffixText, ShowValue, CalloutText1, CalloutText2, DimensionLowerText, CenterText, ConfigOption, ConfigNames)
```

```

System.bool EditDimensionProperties( 
   System.int TolType,
   System.double TolMax,
   System.double TolMin,
   System.string TolMaxFit,
   System.string TolMinFit,
   System.bool UseDocPrec,
   System.int Precision,
   System.int ArrowsIn,
   System.bool UseDocArrows,
   System.int Arrow1,
   System.int Arrow2,
   System.string PrefixText,
   System.string SuffixText,
   System.bool ShowValue,
   System.string CalloutText1,
   System.string CalloutText2,
   System.string DimensionLowerText,
   System.bool CenterText,
   System.int ConfigOption,
   System.object ConfigNames
)
```

```

System.bool EditDimensionProperties( 
   System.int TolType,
   System.double TolMax,
   System.double TolMin,
   System.String^ TolMaxFit,
   System.String^ TolMinFit,
   System.bool UseDocPrec,
   System.int Precision,
   System.int ArrowsIn,
   System.bool UseDocArrows,
   System.int Arrow1,
   System.int Arrow2,
   System.String^ PrefixText,
   System.String^ SuffixText,
   System.bool ShowValue,
   System.String^ CalloutText1,
   System.String^ CalloutText2,
   System.String^ DimensionLowerText,
   System.bool CenterText,
   System.int ConfigOption,
   System.Object^ ConfigNames
) 
```

#### Parameters

*TolType*
:   Type of tolerance as defined in [swTolType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html)

*TolMax*
:   Maximum value for the tolerance

*TolMin*
:   Minimum value for the tolerance

*TolMaxFit*
:   Text for the maximum FIT value when using a fit tolerance type

*TolMinFit*
:   Text for the minimum FIT value when using a fit tolerance type

*UseDocPrec*
:   True to use the document's precision value, false to use value specified for Precision

*Precision*
:   Precision to use for this dimension if UseDocPrec is false

*ArrowsIn*
:   Arrow direction as defined in [swDimensionArrowsSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionArrowsSide_e.html)

*UseDocArrows*
:   True to use the document's arrow types, false to use values specified for Arrow1 and Arrow2

*Arrow1*
:   Type of arrow to use for the first arrow of this dimension as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html) if UseDocArrows is false

*Arrow2*
:   Type of arrow to use for the second arrow of this dimension as defined in swArrowStyle\_e if UseDocArrows is false

*PrefixText*
:   Text to display before the dimension, but on the same line (see **Remarks**)

*SuffixText*
:   Text to display after the dimension, but on the same line (see **Remarks**)

*ShowValue*
:   True to display the value of the dimension in the user interface, false to not

*CalloutText1*
:   Callout text to display above the dimension

*CalloutText2*
:   Callout text to display below the dimension

*DimensionLowerText*
:   Text to display below the dimension line; valid for [display dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) in drawings only

*CenterText*
:   True to center the text in the dimension, false to not

*ConfigOption*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*ConfigNames*
:   Names of the configurations to which to apply these edits (see **Remarks**)

#### Return Value

True if the dimension is modified, false if not

Remarks

PrefixText and SuffixText must not include "/r/n".

This method:

- always changes the dimension's parameters in the active configuration. For example, if you specify swInConfigurationOpts\_e.swSpecifyConfiguration for ConfigOption and do not specify the name of the active configuration in ConfigNames, then the dimension parameters in the active configuration are affected.
- does not support [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.md).

Example

[Modify Dimension Properties (C#)](Modify_Dimension_Properties_Example_CSharp.htm)  
[Modify Dimension Properties (VB.NET)](Modify_Dimension_Properties_Example_VBNET.htm)  
[Modify Dimension Properties (VBA)](Modify_Dimension_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IEditDimensionProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IEditDimensionProperties.md)
