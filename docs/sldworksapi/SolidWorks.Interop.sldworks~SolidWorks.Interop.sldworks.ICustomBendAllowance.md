# ICustomBendAllowance Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance`

Allows access to the custom bend allowance of a feature.
Allows access to the custom bend allowance of a feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ICustomBendAllowance 
```

```

Dim instance As ICustomBendAllowance
```

```

public interface ICustomBendAllowance 
```

```

public interface class ICustomBendAllowance 
```

Remarks

In your application, the [ICustomBendAllowance::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~Type.md) must always be set last, after the other properties of this interface have been set. The property last set automically overrides any previously set ICustomBendAllowance::Type.

For example:

    cba.**Type** = swBendAllowanceTypes\_e.swBendAllowanceDeduction '\*\*\*set first, so will not hold\*\*\*

    '\*\*\*RESET THE VALUES\*\*\*

    cba.**KFactor** = 0.08

    cba.**BendDeduction** = 0.1

    cba.**BendAllowance** = 0.11

    cba.**BendTableFile** = "E:\AAA Projects\sw2025\QA\SP02\Convert To Sheetmetal FUN156195\1-Staal.xls"

    cba.**BendCalculationTableFile** = "E:\AAA Projects\sw2025\QA\SP02\Convert To Sheetmetal FUN156195\1-Staal.xls"

**cba.Type = swBendAllowanceTypes\_e.swBendAllowanceDirect '\*\*\*set last, so holds\*\*\*\***

**The above code sets the ICustomBendAllowance::Type as swBendAllowanceTypes\_e.swBendAllowanceDirect.**

Another example:

    cba.**Type** = swBendAllowanceTypes\_e.swBendAllowanceDeduction '\*\*\*set first, so will not hold\*\*\*

    '\*\*\*RESET THE VALUES\*\*\*

    cba.**KFactor** = 0.08

    cba.**BendDeduction** = 0.1

    cba.**BendAllowance** = 0.11

    cba.**BendTableFile** = "E:\AAA Projects\sw2025\QA\SP02\Convert To Sheetmetal FUN156195\1-Staal.xls"

    cba.**BendCalculationTableFile** = "E:\AAA Projects\sw2025\QA\SP02\Convert To Sheetmetal FUN156195\1-Staal.xls"

**‘cba.**Type **= swBendAllowanceTypes\_e.swBendAllowanceDirect '\*\*\*set last would hold\*\*\*\*   BUT COMMENTED OUT**

**The above code sets the ICustomBendAllowance::Type as swBendAllowanceTypes\_e.swBendAllowanceBendCalculationTable, because the last property set was BendCalculationTableFile.**

The last ICustomBendAllowance property that is set automatically re-sets the type of bend allowance. You can always explicitly specify the [ICustomBendAllowance::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~Type.md), but you must set it after all other properties of this interface have been set.

Example

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)  
[Get All Sheet Metal Feature Data (VB.NET)](Get_All_Sheet_Metal_Feature_Data_Example_VBNET.htm)  
[Get All Sheet Metal Feature Data (C#)](Get_All_Sheet_Metal_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomBendAllowance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
