# SetBetweenTwoPoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBetweenTwoPoints`

Enables or disables the between two points symbol and its texts.
Enables or disables the between two points symbol and its texts.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetBetweenTwoPoints( _
   ByVal Between As System.Boolean, _
   ByVal TextFrom As System.String, _
   ByVal TextTo As System.String _
) 
```

```

Dim instance As IGtol
Dim Between As System.Boolean
Dim TextFrom As System.String
Dim TextTo As System.String
 
instance.SetBetweenTwoPoints(Between, TextFrom, TextTo)
```

```

void SetBetweenTwoPoints( 
   System.bool Between,
   System.string TextFrom,
   System.string TextTo
)
```

```

void SetBetweenTwoPoints( 
   System.bool Between,
   System.String^ TextFrom,
   System.String^ TextTo
) 
```

#### Parameters

*Between*
:   True to enable the between two points symbol, or false to disable it

*TextFrom*
:   Text on the left end of the symbol

*TextTo*
:   Text on the right end of the symbol

Remarks

The TextFrom and TextTo values might be set to empty strings.

This method ignores TextFrom and TextTo if the between value is false (the symbol is being disabled).

Use:

- [IGtol::GetBetweenTwoPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBetweenTwoPoints.md) to determine if this symbol is currently in use
- [IGtol::GetBetweenTwoPointsText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBetweenTwoPointsText.md) to determine the texts that are part of this symbol

Example

[Insert GTol (C#)](Insert_GTol_Example_CSharp.htm)  
[Insert GTol (VB.NET)](Insert_GTol_Example_VBNET.htm)  
[Insert GTol (VBA)](Insert_GTol_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)
