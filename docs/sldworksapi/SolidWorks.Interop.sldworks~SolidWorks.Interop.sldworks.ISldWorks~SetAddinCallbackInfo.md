# SetAddinCallbackInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetAddinCallbackInfo`

Obsolete. Superseded by ISldWorks::SetAddinCallbackInfo2.
Obsolete. Superseded by [ISldWorks::SetAddinCallbackInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetAddinCallbackInfo2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAddinCallbackInfo( _
   ByVal ModuleHandle As System.Integer, _
   ByVal AddinCallbacks As System.Object, _
   ByVal Cookie As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim ModuleHandle As System.Integer
Dim AddinCallbacks As System.Object
Dim Cookie As System.Integer
Dim value As System.Boolean
 
value = instance.SetAddinCallbackInfo(ModuleHandle, AddinCallbacks, Cookie)
```

```

System.bool SetAddinCallbackInfo( 
   System.int ModuleHandle,
   System.object AddinCallbacks,
   System.int Cookie
)
```

```

System.bool SetAddinCallbackInfo( 
   System.int ModuleHandle,
   System.Object^ AddinCallbacks,
   System.int Cookie
) 
```

#### Parameters

*ModuleHandle*
:   Instance handle of the add-in

*AddinCallbacks*
:   Object that includes the add-in callback methods

*Cookie*
:   Add-in ID; this is the same Cookie you specified in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

#### Return Value

True if the add-in callback commands are set, false if if not

Example

'-----------------------------------------

' Module-level variables

Dim iSldWorks                   As SldWorks.SldWorks

Dim iCookie                     As Long

'-----------------------------------------

'Implementation methods of the SwAddin interface

Private Function SwAddin\_ConnectToSW(ByVal ThisSW As Object, ByVal Cookie As Long) As Boolean

    Dim bRet                As Boolean

    

    ' Store reference to SOLIDWORKS session

    Set iSldWorks = ThisSW

    

    ' Store cookie from SOLIDWORKS

    iCookie = Cookie

    

    'Inform SOLIDWORKS about the object that contains the callbacks

    bRet = iSldWorks.SetAddinCallbackInfo(App.hInstance, Me, iCookie)

    ...

    

    SwAddin\_ConnectToSW = True

End Function

'-----------------------------------------

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddCallback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddCallback.md)  
[ISldWorks::CallBack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CallBack.md)  
[ISldWorks::RemoveCallback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveCallback.md)
