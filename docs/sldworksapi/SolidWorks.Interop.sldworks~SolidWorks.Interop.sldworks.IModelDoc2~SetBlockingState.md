# SetBlockingState Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetBlockingState`

Sets the blocking state for the SOLIDWORKS menus.
Sets the blocking state for the SOLIDWORKS menus.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetBlockingState( _
   ByVal StateIn As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim StateIn As System.Integer
 
instance.SetBlockingState(StateIn)
```

```

void SetBlockingState( 
   System.int StateIn
)
```

```

void SetBlockingState( 
   System.int StateIn
) 
```

#### Parameters

*StateIn*
:   State as defined in [swBlockingStates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBlockingStates_e.html)

Remarks

Call [IModelDoc2::ResetBlockingState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetBlockingState.md) to reset the state when the operations are completed.

IMPORTANT: There must be a corresponding call to IModelDoc2::ResetBlockingState for every call to IModelDoc2::SetBlockingState. It is not enough to call IModelDoc2::ResetBlockingState once at the end of a sequence of operations that have called IModelDoc2::SetBlockingState several times.

Example

[Set Blocking State (VBA)](Set_Blocking_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetBlockingState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetBlockingState.md)
