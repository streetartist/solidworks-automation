# InsertBendTableNew Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableNew`

Inserts a new bend table into the model document.
Inserts a new bend table into the model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBendTableNew( _
   ByVal FileName As System.String, _
   ByVal Units As System.String, _
   ByVal Type As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim FileName As System.String
Dim Units As System.String
Dim Type As System.String
Dim value As System.Boolean
 
value = instance.InsertBendTableNew(FileName, Units, Type)
```

```

System.bool InsertBendTableNew( 
   System.string FileName,
   System.string Units,
   System.string Type
)
```

```

System.bool InsertBendTableNew( 
   System.String^ FileName,
   System.String^ Units,
   System.String^ Type
) 
```

#### Parameters

*FileName*
:   File name of this new bend table

*Units*
:   - Millimeters
    - Centimeters
    - Meters
    - Inches
    - Feet

*Type*
:   - Bend Allowance
    - Bend Deduction

#### Return Value

True if the new table is successfully inserted, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::DeleteBendTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteBendTable.md)  
[IModelDoc2::InsertBendTableEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableEdit.md)  
[IModelDoc2::InsertBendTableOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableOpen.md)
