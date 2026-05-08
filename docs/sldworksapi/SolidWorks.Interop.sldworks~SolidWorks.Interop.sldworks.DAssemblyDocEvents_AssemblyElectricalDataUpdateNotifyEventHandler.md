# DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler`

Fired when the SOLIDWORKS software updates the electrical data.
Fired when the SOLIDWORKS software updates the electrical data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler( _
   ByVal saveType As System.Integer _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler( 
   System.int saveType
)
```

```

public delegate System.int DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler( 
   System.int saveType
)
```

#### Parameters

*saveType*
:   - 0 = All streams
    - 2 = From-To list stream
    - 3 = Segment data stream
    - 4 = Wire list stream

Remarks

If developing a C++ application, use [swAssemblyElectricalDataUpdateNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Third-party applications should handle this notification to reload the electrical data from the data streams when the SOLIDWORKS software writes to them. Currently, this event only occurs when a user exits a route.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_AssemblyElectricalDataUpdateNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_AssemblyElectricalDataUpdateNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
