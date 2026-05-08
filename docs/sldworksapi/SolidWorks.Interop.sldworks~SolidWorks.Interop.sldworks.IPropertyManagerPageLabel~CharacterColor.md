# CharacterColor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~CharacterColor`

Gets or sets the color of the specified characters in this PropertyManager label.
Gets or sets the color of the specified characters in this PropertyManager label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CharacterColor( _
   ByVal StartChar As System.Short, _
   ByVal EndChar As System.Short _
) As System.Integer
```

```

Dim instance As IPropertyManagerPageLabel
Dim StartChar As System.Short
Dim EndChar As System.Short
Dim value As System.Integer
 
instance.CharacterColor(StartChar, EndChar) = value
 
value = instance.CharacterColor(StartChar, EndChar)
```

```

System.int CharacterColor( 
   System.short StartChar,
   System.short EndChar
) {get; set;}
```

```

property System.int CharacterColor {
   System.int get(System.short StartChar, System.short EndChar);
   void set (System.short StartChar, System.short EndChar, System.int value);
}
```

#### Parameters

*StartChar*
:   0-based index value of start character

*EndChar*
:   0-based index value of end character

#### Property Value

RGB value for the text color for the specified characters; if not specified, then the system default setting for text color is used

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.md)  
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.md)
