# CompConfigProperties4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties4`

Obsolete. Superseded by IAssemblyDoc::CompConfigProperties5.
Obsolete. Superseded by [IAssemblyDoc::CompConfigProperties5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CompConfigProperties4( _
   ByVal Suppression As System.Integer, _
   ByVal Solving As System.Integer, _
   ByVal Visibility As System.Boolean, _
   ByVal UseNamedRefConfig As System.Boolean, _
   ByVal RefConfigName As System.String, _
   ByVal ExcludeFromBOM As System.Boolean _
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
Dim value As System.Boolean
 
value = instance.CompConfigProperties4(Suppression, Solving, Visibility, UseNamedRefConfig, RefConfigName, ExcludeFromBOM)
```

```

System.bool CompConfigProperties4( 
   System.int Suppression,
   System.int Solving,
   System.bool Visibility,
   System.bool UseNamedRefConfig,
   System.string RefConfigName,
   System.bool ExcludeFromBOM
)
```

```

System.bool CompConfigProperties4( 
   System.int Suppression,
   System.int Solving,
   System.bool Visibility,
   System.bool UseNamedRefConfig,
   System.String^ RefConfigName,
   System.bool ExcludeFromBOM
) 
```

#### Parameters

*Suppression*
:   Suppression state of this component as defined in [swComponentSuppressionState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)

*Solving*
:   Solving state of this component as defined in [swComponentSolvingOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSolvingOption_e.html)

*Visibility*
:   True if you want to show the selected component in the graphics display area, false if not

*UseNamedRefConfig*
:   Not used

*RefConfigName*
:   - If a non-empty string is specified, then the referenced configuration of the selected component is changed to this named configuration
    - If an empty string is specified, then the default referenced configuration is used

*ExcludeFromBOM*
:   True to exclude the configuration from the BOM, false to not

#### Return Value

True if setting the properties of the selected component in the specified configuration is successful, false if not

Remarks

You can use configurations to save certain display characteristics with each of the assembly components and retrieve that configuration in the future. SOLIDWORKS applies the settings that you specify with this method to the active configuration.

You cannot set a component to lightweight.

Known reasons for failure of this method include:

- Invalid suppression state specified.
- Not preselecting a component.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
