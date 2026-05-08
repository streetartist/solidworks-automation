# PostMessageToApplicationx64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PostMessageToApplicationx64`

Posts a message to the application that invoked this method in 64-bit applications.
Posts a message to the application that invoked this method in 64-bit applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PostMessageToApplicationx64( _
   ByVal Cookie As System.Integer, _
   ByVal UserData As System.Long _
) 
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim UserData As System.Long
 
instance.PostMessageToApplicationx64(Cookie, UserData)
```

```

void PostMessageToApplicationx64( 
   System.int Cookie,
   System.long UserData
)
```

```

void PostMessageToApplicationx64( 
   System.int Cookie,
   System.int64 UserData
) 
```

#### Parameters

*Cookie*
:   Cookie specified in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

*UserData*
:   Additional message-specific information defined by the application

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::PostMessageToApplication Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PostMessageToApplication.md)
