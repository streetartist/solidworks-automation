# DPartDocEvents_SuppressionStateChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SuppressionStateChangeNotifyEventHandler`

Fired when the suppression state of a feature changes.
Fired when the suppression state of a feature changes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_SuppressionStateChangeNotifyEventHandler( _
   ByVal Feature As Feature, _
   ByVal NewSuppressionState As System.Integer, _
   ByVal PreviousSuppressionState As System.Integer, _
   ByVal ConfigurationOption As System.Integer, _
   ByRef ConfigurationNames As System.Object _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_SuppressionStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_SuppressionStateChangeNotifyEventHandler( 
   Feature Feature,
   System.int NewSuppressionState,
   System.int PreviousSuppressionState,
   System.int ConfigurationOption,
   ref System.object ConfigurationNames
)
```

```

public delegate System.int DPartDocEvents_SuppressionStateChangeNotifyEventHandler( 
   Feature^ Feature,
   System.int NewSuppressionState,
   System.int PreviousSuppressionState,
   System.int ConfigurationOption,
   System.Object^% ConfigurationNames
)
```

#### Parameters

*Feature*
:   [Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) whose suppression state changed

*NewSuppressionState*
:   New suppression state for the feature as defined by [swFeatureSuppressionAction\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureSuppressionAction_e.html)

*PreviousSuppressionState*
:   New suppression state for the feature as defined by [swFeatureSuppressionAction\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureSuppressionAction_e.html)

*ConfigurationOption*
:   Configuration option as defined by [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*ConfigurationNames*
:   Array of configurations in which the suppression state of the feature changes

Remarks

If developing a C++ application, use [swPartSuppressionStateChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_SuppressionStateChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SuppressionStateChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
