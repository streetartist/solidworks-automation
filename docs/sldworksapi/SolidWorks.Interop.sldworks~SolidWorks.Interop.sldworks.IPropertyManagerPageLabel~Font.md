# Font Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~Font`

Gets or sets the font for the specified characters in this PropertyManager label.
Gets or sets the font for the specified characters in this PropertyManager label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Font( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.String
```

```

Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.String
 
instance.Font(StartChar, EndChar) = value
 
value = instance.Font(StartChar, EndChar)
```

```

System.string Font( 
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

```

property System.String^ Font {
   System.String^ get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.String^ value);
}
```

#### Parameters

*StartChar*
:   0-based index value of start character

*EndChar*
:   0-based index value of end character

#### Property Value

Name of the font to use for the specified characters

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.md)  
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.md)
