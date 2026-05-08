# ShowLines Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ShowLines`

Gets or sets whether the extension lines are shown in this center mark.
Gets or sets whether the extension lines are shown in this center mark.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowLines As System.Boolean
```

```

Dim instance As ICenterMark
Dim value As System.Boolean
 
instance.ShowLines = value
 
value = instance.ShowLines
```

```

System.bool ShowLines {get; set;}
```

```

property System.bool ShowLines {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True shows the lines, false does not

Example

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.md)
