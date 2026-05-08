# SizeRatio Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~SizeRatio`

Gets or sets the size of the specified characters in this PropertyManager label.
Gets or sets the size of the specified characters in this PropertyManager label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SizeRatio( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.Double
```

```

Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.Double
 
instance.SizeRatio(StartChar, EndChar) = value
 
value = instance.SizeRatio(StartChar, EndChar)
```

```

System.double SizeRatio( 
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

```

property System.double SizeRatio {
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

Ratio for the height of the characters relative to their expected heights; >0 increases their heights and <0 decreases their height

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.md)  
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.md)
