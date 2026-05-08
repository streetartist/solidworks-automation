# ConnectionLines Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ConnectionLines`

Gets or sets the visibility of the connection line of this center mark.
Gets or sets the visibility of the connection line of this center mark.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ConnectionLines As System.Integer
```

```

Dim instance As ICenterMark
Dim value As System.Integer
 
instance.ConnectionLines = value
 
value = instance.ConnectionLines
```

```

System.int ConnectionLines {get; set;}
```

```

property System.int ConnectionLines {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

State of the visibility of the connection line as defined in [swCenterMarkConnectionLine\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkConnectionLine_e.html)

Example

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)  
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.md)
