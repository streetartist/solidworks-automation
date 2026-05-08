# GetFromTo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFromTo`

Gets whether the From-To symbol is present in this Gtol.
Gets whether the From-To symbol is present in this Gtol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFromTo() As System.Boolean
```

```

Dim instance As IGtol
Dim value As System.Boolean
 
value = instance.GetFromTo()
```

```

System.bool GetFromTo()
```

```

System.bool GetFromTo(); 
```

#### Return Value

True if From-To symbol is present, false if not

Remarks

The From-To symbol:

- is present below the Gtol frame.
- specifies that the Gtol value applies from one point or entity to another.

If this method returns true, then call [IGtol::GetFromToText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFromToText.md) and [IGtol::SetFromToText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFromToText.md) to retrieve and set the From-To labels for this Gtol.

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)
