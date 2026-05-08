# IEquationMgr Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members`

Maintains a list of all of the existing equations in a model.
The following tables list the members exposed by [IEquationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AngularEquationUnits](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AngularEquationUnits.md) | Gets or sets the angular units used in equations. |
| Property | [AutomaticRebuild](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AutomaticRebuild.md) | Gets or sets whether to automatically rebuild after modifications. |
| Property | [AutomaticSolveOrder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AutomaticSolveOrder.md) | Gets or sets whether to automatically sequence equations in an order determined by SOLIDWORKS to produce accurate results. |
| Property | [Disabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Disabled.md) | Gets or sets whether to disable the specified equation in the model. |
| Property | [Equation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.md) | Gets or sets the equation at the specified index. |
| Property | [FilePath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~FilePath.md) | Gets or sets the path for an exported equation text (**.txt**) file. |
| Property | [GlobalVariable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GlobalVariable.md) | Gets whether the equation at the specified index is a global variable. |
| Property | [LinkToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~LinkToFile.md) | Gets or sets whether the equation is linked to an exported equation text (**.txt**) file. |
| Property | [Status](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Status.md) | Gets the status of the last equation that was executed. |
| Property | [Suppression](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Suppression.md) | Obsolete as of SOLIDWORKS 2014 and later. |
| Property | [Value](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Value.md) | Gets the value of the equation at the specified index. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Add](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add.md) | Obsolete. Superseded by [IEquationMgr::Add2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2.md). |
| Method | [Add2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add2.md) | Adds an equation at the specified index. |
| Method | [Add3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Add3.md) | Adds an equation at the specified index for the specified configurations. |
| Method | [ChangeSuppressionForAllConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForAllConfigurations.md) | Changes the suppression state of the specified equation in all configurations. |
| Method | [ChangeSuppressionForConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ChangeSuppressionForConfiguration.md) | Changes the suppression state of an equation in the specified configuration. |
| Method | [Delete](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Delete.md) | Deletes the equation at the specified index. |
| Method | [EvaluateAll](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~EvaluateAll.md) | Evaluates all equations. |
| Method | [GetConfigurationOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetConfigurationOption.md) | Gets the configuration option for the equation at the specified index. |
| Method | [GetCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetCount.md) | Gets the number of equations in the model. |
| Method | [GetDisabledEquationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~GetDisabledEquationCount.md) | Gets the number of disabled equations in the model. |
| Method | [IAdd3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~IAdd3.md) | Adds an equation at the specified index for the specified configurations. |
| Method | [ISetEquationAndConfigurationOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~ISetEquationAndConfigurationOption.md) | Modifies the equation at the specified index for the specified configurations. |
| Method | [SetEquationAndConfigurationOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~SetEquationAndConfigurationOption.md) | Modifies the equation at the specified index for the specified configurations. |
| Method | [UpdateValuesFromExternalEquationFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~UpdateValuesFromExternalEquationFile.md) | Updates equations dependent on a linked equation file and ensures that the linked equation file exists and updates its current path, if necessary. |

[Top](#top)

 

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
