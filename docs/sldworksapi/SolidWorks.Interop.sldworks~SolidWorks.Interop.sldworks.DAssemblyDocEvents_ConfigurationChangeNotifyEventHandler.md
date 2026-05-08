# DAssemblyDocEvents_ConfigurationChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ConfigurationChangeNotifyEventHandler`

Gets information about an object or feature that has had one of its configurable parameters changed.
Gets information about an object or feature that has had one of its configurable parameters changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ConfigurationChangeNotifyEventHandler( _
   ByVal ConfigurationName As System.String, _
   ByVal Object As System.Object, _
   ByVal ObjectType As System.Integer, _
   ByVal changeType As System.Integer _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ConfigurationChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ConfigurationChangeNotifyEventHandler( 
   System.string ConfigurationName,
   System.object Object,
   System.int ObjectType,
   System.int changeType
)
```

```

public delegate System.int DAssemblyDocEvents_ConfigurationChangeNotifyEventHandler( 
   System.String^ ConfigurationName,
   System.Object^ Object,
   System.int ObjectType,
   System.int changeType
)
```

#### Parameters

*ConfigurationName*
:   Name of the configuration that has changed

*Object*
:   Object that has changed

*ObjectType*
:   Type of the object that has changed as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

    - swSelDIMENSIONS
    - swSelDATUMPOINTS
    - swSelDATUMPLANES
    - swSelDATUMAXES
    - swSelHELIX
    - swSelBODYFEATURES
    - swSelMATEGROUP
    - swSelMATES
    - swSelCOORDSYS
    - swSelCOMPONENTS
    - swSelCONFIGURATIONS
    - swSelSKETCHES
    - swSelREFCURVES
    - swSelDISPLAYSTATE

    All other types are returned as swSelUNSUPPORTED.

*changeType*
:   Type of change as defined by [swConfigurationChangeTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationChangeTypes_e.html)

Remarks

If developing a C++ application, use [swAssemblyConfigurationChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_ConfigurationChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ConfigurationChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
