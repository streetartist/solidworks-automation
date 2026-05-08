# GetTitle Method (IDesignTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~GetTitle`

Gets the design table title.
Gets the design table title.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTitle() As System.String
```

```

Dim instance As IDesignTable
Dim value As System.String
 
value = instance.GetTitle()
```

```

System.string GetTitle()
```

```

System.String^ GetTitle(); 
```

#### Return Value

Design table title

Remarks

This method returns the title of the design table. If the title row is absent, then this method returns an empty string. If the title row exists but there is no title, then this method returns a single space.

Example

[Get Design Table (VBA)](Get_Design_Table_Example_VB.htm)  
[Get Design Table (VB.NET)](Get_Design_Table_Example_VBNET.htm)  
[Get Design Table (C#)](Get_Design_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)
