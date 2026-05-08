# GetIgesErrorCode Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIgesErrorCode`

Gets the current IGES error code.
Gets the current IGES error code.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIgesErrorCode( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IBody2
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.GetIgesErrorCode(Index)
```

```

System.int GetIgesErrorCode( 
   System.int Index
)
```

```

System.int GetIgesErrorCode( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Position of the error within the current list of errors

#### Return Value

IGES error code

Remarks

This method is intended for use during IGES processing only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetIgesErrorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIgesErrorCount.md)
