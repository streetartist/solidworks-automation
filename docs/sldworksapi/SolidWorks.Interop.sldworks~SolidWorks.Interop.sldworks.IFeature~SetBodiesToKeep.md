# SetBodiesToKeep Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetBodiesToKeep`

Set the bodies to keep and their configurations for features that create multiple bodies in parts and assemblies.
Set the bodies to keep and their configurations for features that create multiple bodies in parts and assemblies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetBodiesToKeep( _
   ByVal AllBodies As System.Boolean, _
   ByVal BodiesToKeep As System.Object, _
   ByVal ConfigOption As System.Integer, _
   ByVal ConfigNames As System.Object _
) 
```

```

Dim instance As IFeature
Dim AllBodies As System.Boolean
Dim BodiesToKeep As System.Object
Dim ConfigOption As System.Integer
Dim ConfigNames As System.Object
 
instance.SetBodiesToKeep(AllBodies, BodiesToKeep, ConfigOption, ConfigNames)
```

```

void SetBodiesToKeep( 
   System.bool AllBodies,
   System.object BodiesToKeep,
   System.int ConfigOption,
   System.object ConfigNames
)
```

```

void SetBodiesToKeep( 
   System.bool AllBodies,
   System.Object^ BodiesToKeep,
   System.int ConfigOption,
   System.Object^ ConfigNames
) 
```

#### Parameters

*AllBodies*
:   True to keep all bodies, false to not

*BodiesToKeep*
:   Array of bodies to keep

*ConfigOption*
:   Configuration options as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*ConfigNames*
:   Array of configuration names

Example

[Cut Body and Keep All Bodies (C#)](Cut_Body_and_Keep_All_Bodies_Example_CSharp.htm)  
[Cut Body and Keep All Bodies (VB.NET)](Cut_Body_and_Keep_All_Bodies_Example_VBNET.htm)  
[Cut Body and Keep All Bodies (VBA)](Cut_Body_and_Keep_All_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IAssemblyDoc PromptBodiesToKeepNotify Event](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler.md)  
[IPartDoc PromptBodiesToKeepNotify Event](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_PromptBodiesToKeepNotifyEventHandler.md)
