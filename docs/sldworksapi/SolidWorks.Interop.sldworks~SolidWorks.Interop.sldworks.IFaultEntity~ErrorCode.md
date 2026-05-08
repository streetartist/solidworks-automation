# ErrorCode Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~ErrorCode`

Gets the error for the fault for the specified entity.
Gets the error for the fault for the specified entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ErrorCode( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IFaultEntity
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.ErrorCode(Index)
```

```

System.int ErrorCode( 
   System.int Index
) {get;}
```

```

property System.int ErrorCode {
   System.int get(System.int Index);
}
```

#### Parameters

*Index*
:   0-based index number indicating the entity with the fault

#### Property Value

Error as defined by [swFaultEntityErrorCode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFaultEntityErrorCode_e.html); -1 indicates an unknown error

Remarks

To determine the value for index, call [IFaultEntity::Count](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Count.md) before calling this property. Call [IFaultEntity::Entity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Entity2.md) to get the entity.

Example

[Check Bodies for Faults (VBA)](Check_Bodies_for_Faults_Example_VB.htm)  
[Check Faces for Faults (VBA)](Check_Faces_for_Faults_Example_VB.htm)  
[Check Edges for Faults (C#)](Check_Edges_for_Faults_Example_CSharp.htm)  
[Check Edges for Faults (VB.NET)](Check_Edges_for_Faults_Example_VBNET.htm)  
[Check Edges for Faults (VBA)](Check_Edges_for_Faults_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFaultEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity.md)  
[IFaultEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity_members.md)
