# SetAddinCallbackInfo2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetAddinCallbackInfo2`

Sets add-in callback commands.
Sets add-in callback commands.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAddinCallbackInfo2( _
   ByVal ModuleHandle As System.Long, _
   ByVal AddinCallbacks As System.Object, _
   ByVal Cookie As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim ModuleHandle As System.Long
Dim AddinCallbacks As System.Object
Dim Cookie As System.Integer
Dim value As System.Boolean
 
value = instance.SetAddinCallbackInfo2(ModuleHandle, AddinCallbacks, Cookie)
```

```

System.bool SetAddinCallbackInfo2( 
   System.long ModuleHandle,
   System.object AddinCallbacks,
   System.int Cookie
)
```

```

System.bool SetAddinCallbackInfo2( 
   System.int64 ModuleHandle,
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
:   Add-in ID; this is the same cookie you specify in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

#### Return Value

True if the add-in callback commands are set, false if not

Example

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)  
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::AddCallback Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddCallback.md)  
[ISldWorks::RemoveCallback Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveCallback.md)  
[ISldWorks::CallBack Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CallBack.md)
