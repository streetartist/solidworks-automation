# SetSheetsSelected Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetSheetsSelected`

Sets the specified drawing sheets whose setups to modify.
Sets the specified drawing sheets whose setups to modify.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetSheetsSelected( _
   ByVal NewSheetList As System.Object _
) 
```

```

Dim instance As IDrawingDoc
Dim NewSheetList As System.Object
 
instance.SetSheetsSelected(NewSheetList)
```

```

void SetSheetsSelected( 
   System.object NewSheetList
)
```

```

void SetSheetsSelected( 
   System.Object^ NewSheetList
) 
```

#### Parameters

*NewSheetList*
:   Names of the drawing sheets whose setups to modify (see **Remarks**)

Remarks

The first drawing sheet in the drawing is automatically included in NewSheetList and need not be specified.

After calling this method, call [IDrawingDoc::SetupSheet6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet6.md) to specify how to modify the setups of the specified drawing sheets.

Example

[Modify Multiple Drawing Sheets Setups (C#)](Modify_Multiple_Drawing_Sheets_Setups_Example_CSharp.htm)  
[Modify Multiple Drawing Sheets Setups (VB.NET)](Modify_Multiple_Drawing_Sheets_Setups_Example_VBNET.htm)  
[Modify Multiple Drawing Sheets Setups (VBA)](Modify_Multiple_Drawing_Sheets_Setups_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
