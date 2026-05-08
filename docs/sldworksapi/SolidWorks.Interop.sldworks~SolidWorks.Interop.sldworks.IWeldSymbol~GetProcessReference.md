# GetProcessReference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetProcessReference`

Gets whether there is a reference box around the indication of welding process text.
Gets whether there is a reference box around the indication of welding process text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetProcessReference() As System.Boolean
```

```

Dim instance As IWeldSymbol
Dim value As System.Boolean
 
value = instance.GetProcessReference()
```

```

System.bool GetProcessReference()
```

```

System.bool GetProcessReference(); 
```

#### Return Value

True if there is a reference box around the process text, false if not

Remarks

Get:

- Flag that tells whether or not the indication of welding process flag is set on this weld symbol using [IWeldSymbol::GetProcess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetProcess.md).
- Text related to the indication of welding process using [IWeldSymbol::GetText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetText.md).

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
