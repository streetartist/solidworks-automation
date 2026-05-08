# SetBendState Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetBendState`

Sets the bend state of a sheet metal part.
Sets the bend state of a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBendState( _
   ByVal BendState As System.Integer _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim BendState As System.Integer
Dim value As System.Integer
 
value = instance.SetBendState(BendState)
```

```

System.int SetBendState( 
   System.int BendState
)
```

```

System.int SetBendState( 
   System.int BendState
) 
```

#### Parameters

*BendState*
:   Sheet metal state to set in this part as defined in [swSMBendState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSMBendState_e.html)

#### Return Value

Status of the set operation as defined in [swSMCommandStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSMCommandStatus_e.html) (see **Remarks**)

Remarks

This method only works for old-style sheet metal parts or non-sheet metal parts converted to sheet metal parts. To set the bend state on new-style sheet metal parts (i.e., those that have a base flange as their first feature), suppress and unsuppress the flat-pattern feature.

If editing a part with bend information in the context of the assembly (see [IAssemblyDoc::EditPart2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditPart2.md)), the bend state for that part will be set.

|  |  |
| --- | --- |
| **If this method is executed on...** | **Then...** |
| Part without bend information | The part is not affected, and retval is set to swSMErrorNotASheetMetalPart |
| Assembly | The assembly is not affected, and retval is set to swSMErrorNotAPart |
| NOTE:  In both of these cases, status is S\_false for the COM version of this method. | |

Example

[Flatten Sheet Metal Part (VBA)](Flatten_Sheet_Metal_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetBendState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetBendState.md)
