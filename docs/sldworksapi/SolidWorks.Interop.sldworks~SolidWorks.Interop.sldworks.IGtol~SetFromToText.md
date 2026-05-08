# SetFromToText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFromToText`

Adds a From-To symbol and sets the From-To text for this Gtol.
Adds a From-To symbol and sets the From-To text for this Gtol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFromToText( _
   ByVal EnableFromTo As System.Boolean, _
   ByVal FromText As System.String, _
   ByVal ToText As System.String _
) As System.Boolean
```

```

Dim instance As IGtol
Dim EnableFromTo As System.Boolean
Dim FromText As System.String
Dim ToText As System.String
Dim value As System.Boolean
 
value = instance.SetFromToText(EnableFromTo, FromText, ToText)
```

```

System.bool SetFromToText( 
   System.bool EnableFromTo,
   System.string FromText,
   System.string ToText
)
```

```

System.bool SetFromToText( 
   System.bool EnableFromTo,
   System.String^ FromText,
   System.String^ ToText
) 
```

#### Parameters

*EnableFromTo*
:   True to enable From-To symbol

*FromText*
:   From text label

*ToText*
:   To text label

#### Return Value

True if From-To text successfully set, false if not

Remarks

The From-To symbol:

- is present below the Gtol frame.
- specifies that the Gtol value applies from one point or entity to another.

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetFromToText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFromToText.md)
