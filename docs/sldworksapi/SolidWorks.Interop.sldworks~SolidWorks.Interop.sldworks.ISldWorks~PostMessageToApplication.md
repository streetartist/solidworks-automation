# PostMessageToApplication Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PostMessageToApplication`

Posts a message to the application that invoked this method.
Posts a message to the application that invoked this method.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PostMessageToApplication( _
   ByVal Cookie As System.Integer, _
   ByVal UserData As System.Integer _
) 
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim UserData As System.Integer
 
instance.PostMessageToApplication(Cookie, UserData)
```

```

void PostMessageToApplication( 
   System.int Cookie,
   System.int UserData
)
```

```

void PostMessageToApplication( 
   System.int Cookie,
   System.int UserData
) 
```

#### Parameters

*Cookie*
:   Cookie specified in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

*UserData*
:   Additional message-specific information defined by the application

Remarks

If your application must be x64 compatible, then use [ISldWorks::PostMessageToApplicationx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PostMessageToApplicationx64.md).

Example

Contact SOLIDWORKS API Support to obtain either the 32-bit or 64-bit version of **C++ 32-bit and 64-bit Add-ins Post Messages After Every Selection**.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddCallback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddCallback.md)
