# LineOffset Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~LineOffset`

Gets or sets whether to raise or lower the specified characters above or below their baselines, relative to their heights, in this PropertyManager label.
Gets or sets whether to raise or lower the specified characters above or below their baselines, relative to their heights, in this PropertyManager label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LineOffset( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.Double
```

```

Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.Double
 
instance.LineOffset(StartChar, EndChar) = value
 
value = instance.LineOffset(StartChar, EndChar)
```

```

System.double LineOffset( 
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

```

property System.double LineOffset {
   System.double get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.double value);
}
```

#### Parameters

*StartChar*
:   0-based index value of start character

*EndChar*
:   0-based index value of end character

#### Property Value

Specify:

- 0.0 to show the character on its baseline
- -1.0 to show the character 1 character below its baseline
- +1.0 to show the character 1 character above its baseline

Remarks

Offsetting (i.e., raising or lowering a character above or below its baseline, relative to its height) a character allows you to show that character as a subscript or exponent in an equation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.md)  
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.md)
