# GetErrorMessages Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetErrorMessages`

Gets the last 20 messages issued by SOLIDWORKS in the current SOLIDWORKS session.
Gets the last 20 messages issued by SOLIDWORKS in the current SOLIDWORKS session.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetErrorMessages( _
   ByRef Msgs As System.Object, _
   ByRef MsgIDs As System.Object, _
   ByRef MsgTypes As System.Object _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim Msgs As System.Object
Dim MsgIDs As System.Object
Dim MsgTypes As System.Object
Dim value As System.Integer
 
value = instance.GetErrorMessages(Msgs, MsgIDs, MsgTypes)
```

```

System.int GetErrorMessages( 
   out System.object Msgs,
   out System.object MsgIDs,
   out System.object MsgTypes
)
```

```

System.int GetErrorMessages( 
   [Out] System.Object^ Msgs,
   [Out] System.Object^ MsgIDs,
   [Out] System.Object^ MsgTypes
) 
```

#### Parameters

*Msgs*
:   Array of the last 20 messages issued by SOLIDWORKS in this SOLIDWORKS session

*MsgIDs*
:   Array of the resource IDs of the last 20  messages issued by SOLIDWORKS in this SOLIDWORKS  
    session

*MsgTypes*
:   Array of the types of the last 20 messages issued by SOLIDWORKS in this SOLIDWORKS  
    session (see Remarks)

#### Return Value

Number of messages issued by SOLIDWORKS in this SOLIDWORKS session

**NOTE:**The stack is cleared after calling this method.

Remarks

The elements of the MsgTypes array are bitmasks of the Microsoft message-box system constants.

Example

[Get Messages (VBA)](Get_Messages_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetLastSaveError Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLastSaveError.md)
