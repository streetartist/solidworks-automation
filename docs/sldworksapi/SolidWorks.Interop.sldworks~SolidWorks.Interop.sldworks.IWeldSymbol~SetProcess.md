# SetProcess Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetProcess`

Sets the values related to the indication of welding process for this weld symbol.
Sets the values related to the indication of welding process for this weld symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetProcess( _
   ByVal Process As System.Boolean, _
   ByVal Text As System.String, _
   ByVal Reference As System.Boolean _
) As System.Boolean
```

```

Dim instance As IWeldSymbol
Dim Process As System.Boolean
Dim Text As System.String
Dim Reference As System.Boolean
Dim value As System.Boolean
 
value = instance.SetProcess(Process, Text, Reference)
```

```

System.bool SetProcess( 
   System.bool Process,
   System.string Text,
   System.bool Reference
)
```

```

System.bool SetProcess( 
   System.bool Process,
   System.String^ Text,
   System.bool Reference
) 
```

#### Parameters

*Process*
:   True to set the indication of welding process flag, false to not

*Text*
:   Text related to the indication of welding process

*Reference*
:   True to place a reference box around the process text, false to not

#### Return Value

True if the indication of welding process is set, false if not

Remarks

Get:

- Flag that indicates whether the indication of welding process flag is set on this weld symbol using [IWeldSymbol::GetProcess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetProcess.md).

- Text related to the indication of welding process using [IWeldSymbol::GetText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetText.md).
- Flag that indicates whether a reference box exists around this text using [IWeldSymbol::GetProcessReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetProcessReference.md).

The text and reference box are visible if Process is true.

Example

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)  
[IWeldSymbol::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetText.md)
