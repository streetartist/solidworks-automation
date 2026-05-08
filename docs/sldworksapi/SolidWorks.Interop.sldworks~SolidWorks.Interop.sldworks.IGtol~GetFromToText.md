# GetFromToText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFromToText`

Gets the From-To text of this Gtol.
Gets the From-To text of this Gtol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFromToText( _
   ByRef FromText As System.String, _
   ByRef ToText As System.String _
) As System.Boolean
```

```

Dim instance As IGtol
Dim FromText As System.String
Dim ToText As System.String
Dim value As System.Boolean
 
value = instance.GetFromToText(FromText, ToText)
```

```

System.bool GetFromToText( 
   out System.string FromText,
   out System.string ToText
)
```

```

System.bool GetFromToText( 
   [Out] System.String^ FromText,
   [Out] System.String^ ToText
) 
```

#### Parameters

*FromText*
:   From text label

*ToText*
:   To text label

#### Return Value

True if From-To text successfully retrieved, false if not

Remarks

The From-To symbol:

- is present below the Gtol frame.
- specifies that the Gtol value applies from one point or entity to another.

Before calling this method, use [IGtol::GetFromTo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFromTo.md) to determine whether the From-To symbol is present.

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::SetFromToText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFromToText.md)
