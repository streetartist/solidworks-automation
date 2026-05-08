# AddCallback Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddCallback`

Registers a general purpose callback handler.
Registers a general purpose callback handler.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub AddCallback( _
   ByVal Cookie As System.Integer, _
   ByVal CallbackFunction As System.String _
) 
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim CallbackFunction As System.String
 
instance.AddCallback(Cookie, CallbackFunction)
```

```

void AddCallback( 
   System.int Cookie,
   System.string CallbackFunction
)
```

```

void AddCallback( 
   System.int Cookie,
   System.String^ CallbackFunction
) 
```

#### Parameters

*Cookie*
:   Cookie specified in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

*CallbackFunction*
:   Name of the function to call (see **Remarks**)

Remarks

The callback function has three arguments:

| **Callback function parameter name in example** | **Data Type** | **Description** |
| --- | --- | --- |
| cmd | Integer | Command ID as defined in [swAppCallBackCmd\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppCallBackCmd_e.html) |
| data | Integer | Data related to the event |
| dsp | LPDISPATCH | Not currently used |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::CallBack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CallBack.md)  
[ISldWorks::RemoveCallback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveCallback.md)  
[ISldWorks::SetAddinCallbackInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetAddinCallbackInfo.md)  
[ISldWorks::PostMessageToApplication Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PostMessageToApplication.md)
