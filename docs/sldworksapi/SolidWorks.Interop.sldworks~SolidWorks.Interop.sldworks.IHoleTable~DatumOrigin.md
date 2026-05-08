# DatumOrigin Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~DatumOrigin`

Gets the datum origin annotation for this hole table.
Gets the datum origin annotation for this hole table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property DatumOrigin As DatumOrigin
```

```

Dim instance As IHoleTable
Dim value As DatumOrigin
 
value = instance.DatumOrigin
```

```

DatumOrigin DatumOrigin {get;}
```

```

property DatumOrigin^ DatumOrigin {
   DatumOrigin^ get();
}
```

#### Property Value

Pointer to the [IDatumOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.md) object

Example

[Get Labels of Datum Origin (C#)](Get_Labels_of_Datum_Origin_Example_CSharp.htm)  
[Get Labels of Datum Origin (VB.NET)](Get_Labels_of_Datum_Origin_Example_VBNET.htm)  
[Get Labels of Datum Origin (VBA)](Get_Labels_of_Datum_Origin_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)
