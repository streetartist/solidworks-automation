# Italic Property (IPropertyManagerPageLabel)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~Italic`

Gets or sets whether to italicize the specified range of characters in this PropertyManager label.
Gets or sets whether to italicize the specified range of characters in this PropertyManager label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Italic( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.Boolean
 
instance.Italic(StartChar, EndChar) = value
 
value = instance.Italic(StartChar, EndChar)
```

```

System.bool Italic( 
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

```

property System.bool Italic {
   System.bool get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.bool value);
}
```

#### Parameters

*StartChar*
:   0-based index value of start character

*EndChar*
:   0-based index value of end character

#### Property Value

True to italicize the specified range of characters, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.md)  
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.md)
