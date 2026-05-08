# AssignTagPrefix Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~AssignTagPrefix`

Prefixes the manual datum tags of specified holes with specified text.
Prefixes the manual datum tags of specified holes with specified text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AssignTagPrefix( _
   ByVal Index As System.Integer, _
   ByVal TagPrefix As System.String, _
   ByVal ApplyTo As System.Integer _
) As System.Boolean
```

```

Dim instance As IHoleTable
Dim Index As System.Integer
Dim TagPrefix As System.String
Dim ApplyTo As System.Integer
Dim value As System.Boolean
 
value = instance.AssignTagPrefix(Index, TagPrefix, ApplyTo)
```

```

System.bool AssignTagPrefix( 
   System.int Index,
   System.string TagPrefix,
   System.int ApplyTo
)
```

```

System.bool AssignTagPrefix( 
   System.int Index,
   System.String^ TagPrefix,
   System.int ApplyTo
) 
```

#### Parameters

*Index*
:   Index of row to which to apply TagPrefix

*TagPrefix*
:   Prefix to apply

*ApplyTo*
:   Apply to other holes as defined in [swHoleTableTagPrefixApply\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHoleTableTagPrefixApply_e.html) (see **Remarks**)

#### Return Value

True if prefix successfully assigned, false if not

Remarks

This method:

- is valid only if [IHoleTable::TagStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~TagStyle.md) is set to [swHoleTableTagStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHoleTableTagStyle_e.html).swHoleTable\_ManualTags.
- corresponds to the functionality of the **Assign Tag Prefix** dialog that pops up when you right-click on a hole table row of a manual tag.

If ApplyTo is specified with swHoleTableTagPrefixApply\_e:

- swHoleTableTagPrefixApply\_OnlySpecifiedHole, then only the hole as specified by Index is assigned TagPrefix.
- swHoleTableTagPrefixApply\_AllHolesOfSameSize, then all holes that are the same size as the hole specified by Index are assigned TagPrefix.

When TagPrefix is assigned to only the hole as specified by Index, the numbering of all holes of the same size changes.

For example, if:

- A model view has six holes of two different sizes, and the hole table manual tags are initially labeled:

    AA1, AA2, AA3, AA4, BB1, BB2

- Specify Index with the row index of AA1.
- Specify TagPrefix with "AB".
- Specify ApplyTo with swHoleTableTagPrefixApply\_e.swHoleTableTagPrefixApply\_OnlySpecifiedHole.

After calling this method:

- The hole table manual tags are re-labeled:

    AB1, AA1, AA2, AA3, BB1, BB2

Notice that AA1 is re-labeled to AB1, and AA2 - AA4 are re-numbered to AA1 - AA3. BB1 and BB2 are unchanged.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)
