# GetID Method (ISheet)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetID`

Gets the ID of this drawing sheet.
Gets the ID of this drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetID() As System.Integer
```

```

Dim instance As ISheet
Dim value As System.Integer
 
value = instance.GetID()
```

```

System.int GetID()
```

```

System.int GetID(); 
```

#### Return Value

ID of the drawing sheet

Remarks

Each drawing sheet:

- is assigned a unique ID. This ID does not change if you change the name of the drawing sheet.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm).

Example

[Get ID of Active Configuration or Current Drawing Sheet (VB.NET)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_VBNET.htm)  
[Get ID of Active Configuration or Current Drawing Sheet (VBA)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_VB.htm)  
[Get ID of Active Configuration or Current Drawing Sheet (C#)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)
