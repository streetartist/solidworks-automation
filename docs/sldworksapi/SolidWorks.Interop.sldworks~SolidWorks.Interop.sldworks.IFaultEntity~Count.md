# Count Property (IFaultEntity)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Count`

Gets the number of faults that the entity has.
Gets the number of faults that the entity has.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Count As System.Integer
```

```

Dim instance As IFaultEntity
Dim value As System.Integer
 
value = instance.Count
```

```

System.int Count {get;}
```

```

property System.int Count {
   System.int get();
}
```

#### Property Value

Number of faults

Remarks

The return value has a 0-based index.

Call this property before calling [IFaultEntity::Entity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Entity2.md) and [IFaultEntity::ErrorCode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~ErrorCode.md).

Example

[Check Edges for Faults (VBA)](Check_Edges_for_Faults_Example_VB.htm)  
[Check Faces for Faults (VBA)](Check_Faces_for_Faults_Example_VB.htm)  
[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)  
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)  
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFaultEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity.md)  
[IFaultEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity_members.md)
