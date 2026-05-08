# GetProcess Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetProcess`

Gets whether the indication of welding process flag is set on this weld symbol.
Gets whether the indication of welding process flag is set on this weld symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetProcess() As System.Boolean
```

```

Dim instance As IWeldSymbol
Dim value As System.Boolean
 
value = instance.GetProcess()
```

```

System.bool GetProcess()
```

```

System.bool GetProcess(); 
```

#### Return Value

True if the indication of welding process flag is set, false if not

Remarks

Get:

- Text related to the indication of welding process using [IWeldSymbol::GetText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetText.md).
- Flag that indicates whether a reference box exists around this text using [IWeldSymbol::GetProcessReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetProcessReference.md).

Set all of the indication of welding process values (flag, text, and reference) using [IWeldSymbol::SetProcess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetProcess.md).

Example

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)  
[IWeldSymbol::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetText.md)
