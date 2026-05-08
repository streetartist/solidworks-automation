# CompConfigProperties6 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties6`

Sets the properties for the selected component in the specified configuration.
Sets the properties for the selected [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) in the specified [configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CompConfigProperties6( _
   ByVal Suppression As System.Integer, _
   ByVal Solving As System.Integer, _
   ByVal Visibility As System.Boolean, _
   ByVal UseNamedRefConfig As System.Boolean, _
   ByVal RefConfigName As System.String, _
   ByVal ExcludeFromBOM As System.Boolean, _
   ByVal IsEnvelope As System.Boolean, _
   ByVal SaveAssemblyAsPartOption As System.Integer _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim Suppression As System.Integer
Dim Solving As System.Integer
Dim Visibility As System.Boolean
Dim UseNamedRefConfig As System.Boolean
Dim RefConfigName As System.String
Dim ExcludeFromBOM As System.Boolean
Dim IsEnvelope As System.Boolean
Dim SaveAssemblyAsPartOption As System.Integer
Dim value As System.Boolean
 
value = instance.CompConfigProperties6(Suppression, Solving, Visibility, UseNamedRefConfig, RefConfigName, ExcludeFromBOM, IsEnvelope, SaveAssemblyAsPartOption)
```

```

System.bool CompConfigProperties6( 
   System.int Suppression,
   System.int Solving,
   System.bool Visibility,
   System.bool UseNamedRefConfig,
   System.string RefConfigName,
   System.bool ExcludeFromBOM,
   System.bool IsEnvelope,
   System.int SaveAssemblyAsPartOption
)
```

```

System.bool CompConfigProperties6( 
   System.int Suppression,
   System.int Solving,
   System.bool Visibility,
   System.bool UseNamedRefConfig,
   System.String^ RefConfigName,
   System.bool ExcludeFromBOM,
   System.bool IsEnvelope,
   System.int SaveAssemblyAsPartOption
) 
```

#### Parameters

*Suppression*
:   Suppression state of the selected component as defined in [swComponentSuppressionState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)

*Solving*
:   Solving state of the selected component as defined in [swComponentSolvingOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSolvingOption_e.html)

*Visibility*
:   True if you want to show the selected component in the graphics area, false if not

*UseNamedRefConfig*
:   Not used

*RefConfigName*
:   - If a non-empty string is specified, then the referenced configuration of the selected component is changed to this named configuration
    - If an empty string is specified, then the default referenced configuration is used

*ExcludeFromBOM*
:   True to exclude the configuration from the BOM, false to not

*IsEnvelope*
:   True if the selected component is an envelope, false if not

*SaveAssemblyAsPartOption*
:   Option for the selected component when saving this assembly as a part as defined in [swASMSLDPRTCompPref\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swASMSLDPRTCompPref_e.html)

#### Return Value

True if setting the properties of the selected component in the specified configuration is successful, false if not

Remarks

You can use configurations to save certain display characteristics with each of the assembly components and retrieve that configuration in the future. SOLIDWORKS applies the settings that you specify with this method to the active configuration.

You cannot set the selected component to lightweight using this method.

Known reasons for failure of this method include:

- Invalid suppression state specified in Suppression.
- Not pre-selecting the component.

Example

[Change Component to Envelope (VBA)](Change_Component_to_Envelope_Example_VB.htm)  
[Change Component to Envelope (VB.NET)](Change_Component_to_Envelope_Example_VBNET.htm)  
[Change Component to Envelope (C#)](Change_Component_to_Envelope_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IComponent2::ExcludeFromBOM Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ExcludeFromBOM.md)  
[IComponent2::Solving Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Solving.md)  
[IComponent2::Visible Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.md)  
[IComponent2::ReferencedConfiguration Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedConfiguration.md)  
[IComponent2::IsEnvelope Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsEnvelope.md)  
[IComponent2::SetSuppression2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.md)
